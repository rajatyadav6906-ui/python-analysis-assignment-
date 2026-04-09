class FitnessTracker:
    
    def __init__(self):
        # list to store all activities
        self.activities = []

    def log_activity(self, activity_type, duration, calories):
        """
        Add a new fitness activity
        """
        activity = {
            "type": activity_type,
            "duration": duration,   # in minutes
            "calories": calories
        }
        
        self.activities.append(activity)
        print("Activity added successfully!")

    def calculate_metrics(self):
        """
        Calculate total calories, average duration, and frequency
        """
        total_calories = 0
        total_duration = 0

        for act in self.activities:
            total_calories += act["calories"]
            total_duration += act["duration"]

        count = len(self.activities)

        if count == 0:
            print("No activities found!")
            return

        avg_duration = total_duration / count

        print("\n--- FITNESS METRICS ---")
        print("Total Activities:", count)
        print("Total Calories Burned:", total_calories)
        print("Average Duration:", avg_duration)

    def filter_activities(self, condition):
        """
        Filter activities based on type or condition
        condition example: "running", "yoga", "cycling"
        """
        filtered = []

        for act in self.activities:
            if act["type"].lower() == condition.lower():
                filtered.append(act)

        print(f"\n--- FILTERED ACTIVITIES: {condition} ---")
        for act in filtered:
            print(act)

        if len(filtered) == 0:
            print("No matching activities found.")

    def generate_report(self):
        """
        Full summary report
        """
        print("\n================ FITNESS REPORT ================")

        if len(self.activities) == 0:
            print("No data available.")
            return

        # count activity types
        activity_count = {}

        for act in self.activities:
            t = act["type"]
            activity_count[t] = activity_count.get(t, 0) + 1

        print("Total Activities:", len(self.activities))
        print("\nActivity Breakdown:")

        for key, value in activity_count.items():
            print(key, ":", value)

        # also call metrics inside report
        self.calculate_metrics()


# ------------------ Example Usage ------------------

tracker = FitnessTracker()

tracker.log_activity("Running", 30, 250)
tracker.log_activity("Yoga", 45, 150)
tracker.log_activity("Running", 20, 180)
tracker.log_activity("Cycling", 60, 400)

tracker.calculate_metrics()

tracker.filter_activities("Running")

tracker.generate_report()