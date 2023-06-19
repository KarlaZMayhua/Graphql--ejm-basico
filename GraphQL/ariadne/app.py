from ariadne import make_executable_schema, gql, QueryType, ObjectType
from ariadne.asgi import GraphQL

# schema
type_defs = gql("""
    type Query {
        clientes: [Cliente!]!
    }
    
    type Cliente {
        nombre: String!
        dni: String!
        debe: Float!
    }
""")

# Resolver de clientes
query = QueryType()

@query.field("clientes")
def resolve_clientes(*_):
    
    clientes_data = [
        {"nombre": "Juan Mendoza", "dni": "12345678", "debe": 100.0},
        {"nombre": "Marcos Lopez", "dni": "98765432", "debe": 50.0},
        {"nombre": "Laura Montalvo", "dni": "54321678", "debe": 200.0}
    ]
    
    return clientes_data

# Crea el esquema ejecutable
schema = make_executable_schema(type_defs, query)

app = GraphQL(schema, debug=True)

# Ejecutar el servidor 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
