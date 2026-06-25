import json
from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class UserContext:
    user_id: int
    preferences: Dict[str, Any]

class SaaSSENTINEL:
    def __init__(self):
        self.user_contexts = {}

    def add_user_context(self, user_id: int, preferences: Dict[str, Any]):
        self.user_contexts[user_id] = UserContext(user_id, preferences)

    def query(self, query_string: str):
        query_parts = query_string.split()
        if query_parts[0] == 'get':
            if query_parts[1] == 'user':
                if query_parts[2] == 'preferences':
                    # Find 'for user <id>' pattern - look for 'user' AFTER 'for'
                    if 'for' in query_parts:
                        for_index = query_parts.index('for')
                        # Check if there's 'user' after 'for'
                        if for_index + 2 < len(query_parts) and query_parts[for_index + 1] == 'user':
                            user_id = int(query_parts[for_index + 2])
                            if user_id in self.user_contexts:
                                return self.user_contexts[user_id].preferences
                            else:
                                raise ValueError(f"User {user_id} does not exist")
                        else:
                            raise ValueError(f"Invalid query: {query_string}")
                    else:
                        raise ValueError(f"Invalid query: {query_string}")
                else:
                    raise ValueError(f"Invalid key: {query_parts[2]}")
            else:
                raise ValueError(f"Invalid query: {query_string}")
        else:
            raise ValueError(f"Invalid query: {query_string}")

    def fuzzy_query(self, query_string: str) -> Optional[Dict[str, Any]]:
        query_lower = query_string.lower()
        
        # Handle "user preferences" pattern - return first user's preferences
        if 'user' in query_lower and 'preference' in query_lower:
            if self.user_contexts:
                # Return the first user's preferences
                first_user_id = list(self.user_contexts.keys())[0]
                return self.user_contexts[first_user_id].preferences
        
        # Fall back to substring matching in keys/values
        for user_id, user_context in self.user_contexts.items():
            for key, value in user_context.preferences.items():
                if query_lower in key.lower() or query_lower in str(value).lower():
                    return user_context.preferences
        
        return None
