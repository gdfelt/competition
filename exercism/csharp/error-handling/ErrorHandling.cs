using System;

public static class ErrorHandling
{
    public static void HandleErrorByThrowingException()
    {
        throw new Exception("You need to implement this function.");
    }

    public static int? HandleErrorByReturningNullableType(string input)
    {
        try {
            return Int32.Parse(input);
        }
        catch (FormatException){
            return null;
        }

    }

    public static bool HandleErrorWithOutParam(string input, out int result)
    {
        try {
            result = Int32.Parse(input);
            return true;
        }
        catch(FormatException){
            result = 0;
            return false;
        }
    }

    public static void DisposableResourcesAreDisposedWhenExceptionIsThrown(IDisposable disposableObject)
    {
        disposableObject.Dispose();
        throw new Exception("");
    }
}
