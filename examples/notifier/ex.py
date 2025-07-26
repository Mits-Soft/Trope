from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field

# === Metamodelo ===

@dataclass
class Property:
    name: str
    type: str
    metadata: Dict[str, str] = field(default_factory=dict)
    default_value: Any = None
    comment: Optional[str] = None

@dataclass
class DataModelDef:
    name: str
    properties: List[Property]

@dataclass
class MethodDef:
    name: str
    params: List[tuple[str, str]]  # (nombre, tipo)
    return_type: str
    metadata: Dict[str, str] = field(default_factory=dict)
    comment: Optional[str] = None

@dataclass
class ClassDef:
    name: str
    class_type: str  # ej: "Service", "Entity", etc.
    value: str

@dataclass
class EntityDescriptor:
    name: str
    doc: Optional[str] = None
    alias: Optional[str] = None
    imports: List[str] = field(default_factory=list)
    extends: List[str] = field(default_factory=list)
    mixins: List[str] = field(default_factory=list)
    id_props: List[Property] = field(default_factory=list)
    physic_props: List[Property] = field(default_factory=list)
    logic_props: List[Property] = field(default_factory=list)
    security_props: List[Property] = field(default_factory=list)
    classes: List[ClassDef] = field(default_factory=list)
    data_model: List[DataModelDef] = field(default_factory=list)
    methods: List[MethodDef] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convierte el descriptor a un diccionario (como el JSON original, pero más completo)."""
        return {
            "name": self.name,
            "doc": self.doc,
            "imports": self.imports,
            "classes": {cls.name: cls.value for cls in self.classes},
            "dataModel": {
                dm.name: {
                    prop.name: {
                        "type": prop.type,
                        "metadata": prop.metadata,
                        "default": prop.default_value
                    } for prop in dm.properties
                } for dm in self.data_model
            },
            "methods": [
                {
                    "name": m.name,
                    "params": m.params,
                    "return": m.return_type,
                    "metadata": m.metadata
                } for m in self.methods
            ],
            "connections": self._infer_connections()
        }

    def _infer_connections(self) -> List[Dict[str, str]]:
        """Infiere conexiones basadas en DataModel (relaciones entre entidades)."""
        connections = []
        for dm in self.data_model:
            for prop in dm.properties:
                if prop.type == "ReferenceType":
                    connections.append({
                        "source": dm.name,
                        "target": prop.name,
                        "type": "reference"
                    })
        return connections


# === Constructor rápido ===

def create_user_domain() -> EntityDescriptor:
    return EntityDescriptor(
        name="UserDomain",
        doc="Domain for user management and related services.",
        imports=["UserManager"],
        classes=[
            ClassDef(name="UserManager", class_type="Service", value="UserService")
        ],
        data_model=[
            DataModelDef(
                name="UserManager",
                properties=[
                    Property(
                        name="NotificationService",
                        type="ReferenceType",
                        metadata={"relatedConcept": "ExternalService"}
                    ),
                    Property(
                        name="UserRepository",
                        type="ReferenceType",
                        metadata={"relatedConcept": "Persistence"}
                    )
                ]
            )
        ],
        methods=[
            MethodDef(
                name="sendNotification",
                params=[("User", "User"), ("Message", "string")],
                return_type="void",
                metadata={"designPattern": "Observer"}
            ),
            MethodDef(
                name="saveUser",
                params=[("User", "User")],
                return_type="bool",
                metadata={"securityLevel": "High"}
            )
        ],
        id_props=[
            Property(name="domainId", type="string")
        ],
        logic_props=[
            Property(name="isActive", type="bool", default_value=True),
            Property(name="maxRetries", type="int", default_value=3)
        ],
        security_props=[
            Property(name="authRequired", type="bool", default_value=True),
            Property(name="encryptionLevel", type="string", default_value="AES-256")
        ]
    )


# === Ejecución ===

if __name__ == "__main__":
    domain = create_user_domain()
    import json
    print(json.dumps(domain.to_dict(), indent=2))