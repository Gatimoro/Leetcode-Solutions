class Solution:#THIS PROGRAM CALCULATES THE POSITIONS OF OBJECTS INSIDE A BOX AFTER FLIPPING IT 90 DEGREES CLOCKWISE
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        leg=len(box[0])
        fin=[[] for x in range(leg)]
      #ROWS WILL BECOME COLUMNS AND THE LAST ROW WILL BE THE FIRST COL SO WE START FROM IT
        for x in box[::-1]:
            c=0
            rock=0
          #NOW FOR EACH ROW, WE ESSENTIALLY CALCULATE WHERE WILL EVERYTHING BE IN THE ROW WHILE SIMULTANEOUSLY ADDING IT TO THE FINAL MATRIX
            while c+rock<leg:
              #rock KEEPS TRACK OF HOW MANY ROCK DO WE HAVE, WHILE c IS THE INDEX OF THE TILE WHOSE VALUE WE ARE TRYING TO WORK OUT.
                while c+rock<leg and x[c+rock]=='#':
                  #AS LONG AS WE HAVE A STREAK OF ROCK, WE COUNT THEM
                    rock+=1
                #IF THE STREAK OF ROCKS WAS THE LAST THING WE SAW, WE ADD THAT MANY ROCKS TO THE END OF THE COLUMN
                if c+rock==leg:
                    for crock in range(rock):
                        fin[c].append('#')
                        c+=1
                    rock=0
                    break
                #IF WE ENCOUNTER AN INMOVABLE OBJECT '*', WE PRETTY MUCH DO THE SAME AND PILE UP HOWEVERMANY ROCK WE COUNTED DIRECTLY ABOVE IT.
                elif x[c+rock]=='*':
                    for crock in range(rock):
                        fin[c].append('#')
                        c+=1
                    fin[c].append('*')
                    rock=0
                #WHEN WE SEE A FREE SPACE '.', OUT PILE OF ROCK KEEPS 'FALLING' AND THE TOP TILE, INDEXED c BECOMES EMPTY ('.').
                else:
                    fin[c].append('.')
                c+=1
            #FINALLY, IF WE FIND OURSELVES IN A POSITION WHERE WE DIDN'T PLACE ALL ROCKS AFTER EXITING THE LOOP, WE PLACE THEM AT THE BOTTOM OF THE COL.
            if rock:
                for crock in range(rock):
                    fin[c].append('#')
                    c+=1
        return fin
