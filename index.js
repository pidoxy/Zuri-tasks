

const performArithmeticOperation = (num1, num2, symbol) => {
  
    if(symbol === "+"){
        return num1 + num2;
    } else if(symbol === "-"){
        return num1 - num2;
    } else if(symbol === "/"){
        return num1/num2;
    } else if(symbol === "*"){
        return num1*num2;
    }
}

performArithmeticOperation(2,3, String("+"))
performArithmeticOperation(7,2, String("-"))
performArithmeticOperation(6,3, String("/"))
performArithmeticOperation(7,2, String("*"))