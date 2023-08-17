#!/usr/bin/node
// searches for second biggest int in the arguments list and prints it

function secondHigh (argList) {
  if (argList.length === 2 || argList.length === 3) { return (0); }

  let highest = argList[2];
  let secHighest = argList[3];

  for (let i = 2; i < argList.length; i++) {
    if (argList[i] > highest) {
      secHighest = highest;
      highest = argList[i];
    } else if (argList[i] > secHighest && argList[i] < highest) {
      secHighest = argList[i];
    }
  }
  return (secHighest);
}

console.log(secondHigh(process.argv));
