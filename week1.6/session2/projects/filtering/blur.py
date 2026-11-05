from image import Image
import sys

inputFile = input("Input: ")
outputFile = input("Output: ")



def blur(inputFile, outputFile):
    inputImage = Image()
    inputImage.read_pgm(inputFile)
    outputImage = Image.create(inputImage.width, inputImage.height)
    sum = 0 
    average = 0 
    for row in range(1, inputImage.height - 1):
        for col in range(1, inputImage.width - 1):
            if (col + 2) % 3 == 0 and (row+2)%3==0:
                sum = 0 
                average = 0 
                for i in range(3):
                    for j in range(3):
                        sum += inputImage.get((row - 1 + i), (col - 1 + j))
                average = sum // 9
                for i in range(3):
                    for j in range(3):
                        outputImage.set((row - 1 + i), (col - 1 + j), average)

    outputImage.write_pgm(outputFile)

blur(inputFile, outputFile)