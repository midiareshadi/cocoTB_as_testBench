def python_FA_model(a,b,cin):
    sum = a ^ b ^ cin
    cout = (a & b) | (a & cin) | (b & cin)
    return sum, cout