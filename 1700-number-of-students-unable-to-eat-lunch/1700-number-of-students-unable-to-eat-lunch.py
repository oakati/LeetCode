class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        counter = 0
        len_students = len(students)
        while counter < len_students:
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
                counter = 0
            else:
                students = students[1:] + [students[0]]
                counter = counter + 1
            len_students = len(students)
        return len(students)