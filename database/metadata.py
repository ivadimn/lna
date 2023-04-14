class OrgsTable:
    NAME = "orgs"

    class Columns:
        ID = "id"
        NAME = "name"
        FULL_NAME = "full_name"


schema_data = {
    "Data": {"table": "table_name", "fields": ("id", "name", "email")},
    "Org": OrgsTable,
}