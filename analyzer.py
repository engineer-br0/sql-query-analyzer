from sqlparse import parse

import rules

def analyze_query(query):
    suggestions = []
    
    if(query == ""):
        return ["qurry is empty!"]
    
    parsed = parse(query)
    print("parsed ", parsed)
    
    statement = parsed[0]
    print("parsed 0 ", parsed[0])
    
    query_upper = query.upper()
    
    # RULE 1
    result = rules.check_start_with_star(query_upper)
    
    if result:
        suggestions.append(result)
    
    result = rules.check_where_clause(query_upper)
    if result:
        suggestions.append(result)
    
    result = rules.check_limit_clause(query_upper)
    if result:
        suggestions.append(result)
        
    result = rules.check_order_by(query_upper)
    if result:
        suggestions.append(result)
        
    if len(suggestions) == 0:
        return ["Query is perfect"]
    
    return suggestions