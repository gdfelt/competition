using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

public static class Tournament
{   

    private class Team : IComparable {

        public string name = "";
        public int matches = 0;
        public int wins = 0;
        public int draws = 0;
        public int losses = 0;
        public int points = 0;

        public Team(string _name){
            name = _name;
        }

        public void addWin(){
            matches += 1;
            wins += 1;
            points += 3;
        }

        public void addDraw(){
            matches += 1;
            draws += 1;
            points += 1;
        }

        public void addLoss(){
            matches += 1;
            losses += 1;
        }

        int IComparable.CompareTo(object obj){
            Team _team = (Team)obj;
            if(_team.points < this.points){
                return -1;
            }else if(_team.points > this.points){
                return 1;
            } else {
                return String.Compare(this.name, _team.name);
            }
        }

    }
    

    public static void Tally(Stream inStream, Stream outStream)
    {
        
        Dictionary<string, Team> teamData = ReadData(inStream);
        WriteData(teamData, outStream);
        teamData = new Dictionary<string, Team>();
    }


    private static Dictionary<string, Team> ReadData(Stream inStream){

        Dictionary<string, Team> data = new Dictionary<string, Team>();

        using (StreamReader sr = new StreamReader(inStream)){

            string gameLine;
            
            while((gameLine = sr.ReadLine()) != null){

                string[] tokens = gameLine.Split(";");
                
                if(!data.ContainsKey(tokens[0])){
                    data.Add(tokens[0], new Team(tokens[0]));
                }

                if(!data.ContainsKey(tokens[1])){
                    data.Add(tokens[1], new Team(tokens[1]));
                }

                if(tokens[2] == "win"){
                    data[tokens[0]].addWin();                    
                    data[tokens[1]].addLoss();

                }else if(tokens[2] == "loss"){
                    data[tokens[1]].addWin();
                    data[tokens[0]].addLoss();

                }else if(tokens[2] == "draw"){
                    data[tokens[0]].addDraw();
                    data[tokens[1]].addDraw();

                }

            }
        } 
        
        return data;
    }


    private static void WriteData(Dictionary<string, Team> data, Stream _outStream){

        using (StreamWriter sw = new StreamWriter(_outStream)){

            sw.Write(String.Format("{0,-30} | {1,2} | {2,2} | {3,2} | {4,2} | {5,2}", "Team", "MP", "W", "D", "L", "P"));

            List<Team> values = data.Values.ToList();
            values.Sort();
            foreach(var val in values){
                sw.Write(String.Format("\n{0,-30} | {1,2} | {2,2} | {3,2} | {4,2} | {5,2}", val.name, val.matches, val.wins, val.draws, val.losses, val.points));

            }

        }


    }



}
