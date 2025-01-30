class RecommendationSystem:
    def __init__(self):
        # Hash table to store user preferences where key is user_id and value is a list of product_ids
        self.user_preferences = {}

    def add_user(self, user_id):
        """Register a new user in the system."""
        if user_id not in self.user_preferences:
            self.user_preferences[user_id] = []

    def add_preference(self, user_id, product_id):
        """Add a product preference for a specific user."""
        if user_id in self.user_preferences:
            if product_id not in self.user_preferences[user_id]:
                self.user_preferences[user_id].append(product_id)
        else:
            raise ValueError("User does not exist. Please register the user first.")

    def recommend_products(self, user_id):
        """Return a list of recommended products based on user preferences."""
        return self.user_preferences.get(user_id, [])

# Example usage
rec_sys = RecommendationSystem()
rec_sys.add_user("user1")
rec_sys.add_preference("user1", "productA")
rec_sys.add_preference("user1", "productB")
print("Recommended products for user1:", rec_sys.recommend_products("user1"))
