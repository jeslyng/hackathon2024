class EndCredits(Scene):
    def construct(self):
        text1 = Text("Credits:")
        text2 = Text("Manim and TripShot")
        group = VGroup(text1, text2).arrange(DOWN,buff = 0.2).shift(UP)
        self.play(Write(group), run_time=5)
        self.wait(2)
