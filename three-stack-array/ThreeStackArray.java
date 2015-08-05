/*
 * If there were only two stacks you could start at either end and iterate towards the center
 * Since the values of an int[] are all initialized to 0 I can't tell whether an element has been assigned a value
 * An array of objects would be initialized to null, so I could iterate each "stack" at a different increment
 */
class ThreeStackArray {
    public int[] array;
    private int first, second, third;
    private int[] stackPositions = new int[3];

    public ThreeStackArray(int size) {
        array = new int[size];
    }

    public static void main(String[] args) {
        ThreeStackArray stacks = new ThreeStackArray(30);
        for (int key : stacks.array) {
            System.out.println(key);
        }
    }

    public int pop() {
        return 0;
    }

    public int peek() {
        return 0;
    }

    public void push(int stack, int value) {
        int position = stackPositions[stack];
    }
}
