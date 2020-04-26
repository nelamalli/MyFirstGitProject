class  personBehavior:
    emotion = "very angry"
    def f(self):

        return self.emotion

def main():

    m= personBehavior()
    a = m.f
    print(type(a))

main()