import dictest

class Test_Dictest_Pas:
    def test_pas_1(self):
        result = dictest.pas("accessdenied4u")

    def test_pas_2(self):
        result = dictest.pas("NoWiFi4you")

    def test_pas_3(self):
        result = dictest.pas("YouarenotAllowed2Use")

    def test_pas_4(self):
        result = dictest.pas("$p3onyycat")

    def test_pas_5(self):
        result = dictest.pas("!Lov3MyPianoPony")

    def test_pas_6(self):
        result = dictest.pas("")

