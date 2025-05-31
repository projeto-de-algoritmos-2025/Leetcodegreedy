class Solution(object):
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x: x[1])
        
        total_time = 0
        selected_courses = []

        for duration, lastDay in courses:
            total_time += duration
            selected_courses.append(duration)
            if total_time > lastDay:
                longest = max(selected_courses)
                selected_courses.remove(longest)
                total_time -= longest

        return len(selected_courses)