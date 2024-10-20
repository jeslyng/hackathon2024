class EndCredits(Scene):
    def construct(self):
        text1 = Text("We used Manim in this project")
        text2 = Text("which is an open-source Python")
        text3 = Text("library created by 3Blue1Brown.")
        group = VGroup(text1, text2, text3).arrange(DOWN,buff = 0.2).shift(UP)
        self.play(Write(group), run_time=5)
        self.wait(2)
