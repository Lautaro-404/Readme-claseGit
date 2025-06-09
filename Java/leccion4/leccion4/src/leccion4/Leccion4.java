package leccion4;

public class Leccion4 {

    public static void main(String[] args) {
        /*
        // Inferencia de tipos con var y tipos primitivos
        var numEntero = 20; // Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; // Automaticamente con el punto se transforma en tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
        */
        
        // Tipos primitivos char
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024'; // Indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; // Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; // Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 = '\u0024'; // Indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        var varCaracterDecimal1 = (char)36; // Valor Entero y le asigna un tipo int
        System.out.println("varCaracterDecimal = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; // Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$'; 
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);
        
        
    }

}
