using System;

public static class ResistorColor
{

    public static int ColorCode(string color)
    {
        int colorCode = -1;
        switch (color.ToLower())
        {
            case "black":
                colorCode = 0;
                break;
            case "orange":
                colorCode = 3;
                break;
            case "white":
                colorCode = 9;
                break;
        }
        return colorCode;
    }

    public static string[] Colors()
    {
        return new[] { "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white" };
    }
}