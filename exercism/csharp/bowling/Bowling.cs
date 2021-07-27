using System;

public class BowlingGame
{
    // private int runningScore = 0;
    private int[] frameScore = new int[10];
    private int frameIndex = 0;
    private bool openFrame = false;
    private bool priorFrameSpare = false;
    // private bool priorFrameStrike = false;

    public void Roll(int pins) 
    {
        // throw new NotImplementedException("You need to implement this function.");
        if(pins < 0 || pins > 10){
            throw new ArgumentException("Roll cannot be negative or greater than 10");
        }

        if(priorFrameSpare){
            frameScore[frameIndex -1] += pins;
            priorFrameSpare = false;
        }

        // First roll of the frame
        if(!openFrame){
            frameScore[frameIndex] += pins;


            if(pins == 10){

                frameIndex += 1;
                openFrame = false;

            }else{
                openFrame = !openFrame;
                
            }

        // Second Roll of the frame
        } else {
            if(frameScore[frameIndex] + pins > 10 && frameIndex != 9){
                throw new ArgumentException("Frame total cannot exceed 10");
            }

            frameScore[frameIndex] += pins;

            if(frameScore[frameIndex] == 10){
                priorFrameSpare = true;
            }

            if(frameIndex != 9){

                frameIndex += 1;
                openFrame = false;
            }

        }

    }

    public int? Score()
    {
        // throw new NotImplementedException("You need to implement this function.");
        
        int total = 0;
        foreach(int s in frameScore){
            total += s;
        }
        return total;
    }
}