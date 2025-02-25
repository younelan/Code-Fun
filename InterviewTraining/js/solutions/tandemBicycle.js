/*
Tandem Bicycle Challenge 🚲

You're organizing a unique bicycle race event where teams of red-shirted and blue-shirted 
riders must pair up on tandem bicycles. However, there's a twist in how the bicycles work!

The Problem:
Each tandem bicycle has two riders, but the bicycle's speed is determined by the faster
pedaler - not the average speed of both riders. As the event organizer, you need to either
maximize or minimize the total speed of all bicycle pairs, depending on the event type.

Real-World Scenario:
Imagine you're running two different events:
1. Speed Race (fastest = true): You want the fastest possible combined speed
2. Training Session (fastest = false): You want to keep speeds moderate for beginners

How Tandem Bikes Work:
- Two riders on one bike (one red shirt, one blue shirt)
- If Red rider pedals at speed 5 and Blue rider at speed 3
- The bike moves at speed 5 (the faster rider's speed)
- Each rider must be paired with someone wearing the other color

Example Event:

Red Team Speeds:  [5, 5, 3, 9, 2]    // These are your red-shirt riders
Blue Team Speeds: [3, 6, 7, 2, 1]    // These are your blue-shirt riders

Speed Race (fastest = true):
- Best strategy: Pair fastest with slowest
- Pairing: [9,2], [5,7], [5,6], [3,3], [2,1]
- Each pair contributes its max speed: 9 + 7 + 6 + 3 + 2 = 32
- Total Event Speed: 32

Training Session (fastest = false):
- Best strategy: Pair similar speeds together
- Pairing: [9,7], [5,6], [5,3], [3,2], [2,1]
- Each pair contributes its max speed: 9 + 6 + 5 + 3 + 2 = 25
- Total Event Speed: 25

Your Task:
Write a function that takes in both teams' speeds and an event type (fastest),
and returns the optimal total speed based on the best possible pairings.

Function Signature:
tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)

Tips:
1. Try sorting the arrays - it might help with pairing strategies
2. Think about when you want fastest riders together vs separated
3. Remember: each bike's speed is determined by its faster rider

Good luck with your event planning! 
*/

function tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) {
    // Sort both arrays
    const sortedRed = redShirtSpeeds.sort((a, b) => a - b);
    const sortedBlue = blueShirtSpeeds.sort((a, b) => a - b);
    
    let totalSpeed = 0;
    const length = sortedRed.length;
    
    // For fastest=true, we want to pair highest with lowest
    // For fastest=false, we want to pair similar speeds together
    for (let i = 0; i < length; i++) {
        const redIndex = fastest ? length - 1 - i : i;
        const blueIndex = i;
        
        // Take the maximum speed between the paired riders
        const speedAtIndex = Math.max(
            sortedRed[redIndex],
            sortedBlue[blueIndex]
        );
        
        totalSpeed += speedAtIndex;
    }
    
    return totalSpeed;
}

module.exports = tandemBicycle;
