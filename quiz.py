from pprint import pprint

class ProcessFile:
    def __init__(self, lines):
        self.lines = lines
        self.data = self._generate()
        # self._printQuestions()
        # pprint(self.data)

    def _printQuestions(self):
        print "**" * 20
        pprint(self.data['questions'])
        print "**" * 20
        pprint(self.data['answers'])

    def _generate(self):
        result = {}
        questions = []
        answers = []

        # find the first question
        index = 0
        while not self.lines[index].startswith('* '):
            index += 1

        for i in range(index, len(self.lines)):
            # End of question is detected by a new line
            fullQuestion = ''

            while i < len(self.lines[i]) and self.lines[i] == "":
                print self.lines[i]

                question = self.lines[i].strip('* ').rstrip('\n')
                i += 1
                if fullQuestion == '':
                    fullQuestion = question
                else:
                    fullQuestion += '\n' + question

            print "Full Question: " + str(fullQuestion)

            # Get the answer to this question
            fullAnswer = ''
            while i < len(self.lines) and not self.lines[i].startswith('* '):
                answer = self.lines[i].rstrip('\n')
                i += 1

                if fullAnswer == '':
                    fullAnswer = answer
                else:
                    fullAnswer += '\n' + answer

            questions.append(fullQuestion)
            answers.append(fullAnswer)

        result['questions'] = questions
        result['answers'] = answers
        result['count'] = len(questions)

        return result

class QuizManager:
    def __init__(self, data):
        self.data = data
        self.noQ = len(self.data)
        self.needReview = {}
        self.currQ = 0

    def ask_next_question(self):
        print """
        Question: """

        qa = self.data[self.current]


if __name__ == "__main__":
    lines = []

    with open("cs348.txt") as f:
        lines.append(f.readlines())
    f.close()

    file = ProcessFile(lines[0])
