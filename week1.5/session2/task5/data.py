# Week 1.5, Session 2: Task 5

class Dataset:
    """
    A numeric dataset, loaded from a file.
    """

    def __init__(self, filename=None):
        """
        Creates a Dataset containing data from the specified file.

        If no file is specified, an empty Dataset is created.
        """
        self.data = []
        if filename:
            self.load_data(filename)

    def load_data(self, filename):
        """
        Loads data from the specified file into this Dataset.

        Any existing data will be deleted.
        """

        with open(filename,'r') as file:
            data = file.readlines()
            data = [ line.strip().split(",") for line in data]

        self.data = data

    def __len__(self):
        """
        Returns the size of this Dataset.
        """
        length = 0
        for i in self.data:
            length +=1
        return length

    def __getitem__(self, index):
        """
        Returns the value at the specified position in this Dataset.
        """
        return self.data[index]

    def mean(self):
        """
        Returns the arithmetic mean of the values in this Dataset.
        """
        sum = 0
        for i in range(len(self.data)):
            sum += self.data[i]

        return sum / len(self.data)

    def median(self):
        """
        Returns the median of the values in this Dataset.
        """

        median = 0
        orderedNum = sorted(self.data)
        
        if len(self.data) % 2 != 0:
            median = orderedNum[(len(self.data) // 2)]
        else:
            median = ((orderedNum[len(self.data)//2 - 1]) + (orderedNum[len(self.data)//2])) / 2

        return median
