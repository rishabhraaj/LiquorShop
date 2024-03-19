class MyValidate:
    def required(slef,frm):
        for f in frm:
            if f=="":
                return False
        return True