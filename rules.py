
def check_start_with_star(query):
    print("inside check * ", query)
    if("SELECT * FROM" in query):
        print("check true")
        return "avoid using SELECT *. specify required columns.!"
    print("check false")
    return None

def check_where_clause(query):
    if "SELECT" in query and "WHERE" not in query:
        return "given query has no WHERE clause. It may scan entire table = slow performance!"
    
    return None

def check_limit_clause(query):
    if("SELECT" in query and "LIMIT" not in query):
        return "Consider adding LIMIT to restrict result size!"
    return None

def check_order_by(query):
    if("ORDER BY" in query and "CREATE INDEX" not in query):
        return "Ensure ORDER BY column is indexed for better performance."
    
    return None