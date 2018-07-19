export class submissionInterests {
    interests: string[] = [];
    food: string[] = [];
    timeIn: string;
    timeOut: string;

    addInterestsNode(node: string): void {
        this.interests.push(node);
    }

    addFoodNode(node: string): void {
    	this.food.push(node);
    }

    setTimeIn(node: string): void {
    	this.timeIn = node;
    }

    setTimeOut(node: string): void {
    	this.timeOut = node;
    }
    
}