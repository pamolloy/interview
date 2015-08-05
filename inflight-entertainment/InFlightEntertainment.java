import java.util.Arrays;

/*
 * This solution could be optimized by storing the values of movie lengths in a hash map as we
 * traverse the array for the first time
 */
class InFlightEntertainment {

    public void InFlightEntertainment() {

    }

    public static void main(String[] args) {
        int[] movies = {64, 82, 89, 89, 73, 98, 120, 52};
        int flightLength = 100;

        InFlightEntertainment ife = new InFlightEntertainment();
        ife.matchFlightLength(flightLength, movies);
    }

    /*
     * Based on the length of the flight, determine if the length of any two movies equals the
     * flight length. Make sure that the same movie isn't selected twice
     */
    public boolean matchFlightLength(int flightLength, int[] movies) {
        // Stop sorting when the movie length > flight length
        int[] sortedMovies = this.sortMovies(movies, flightLength);
        System.out.println("Sorted array: " + Arrays.toString(sortedMovies));
        return false;
    }

    /*
     * Sort the array of integers using merge sort and remove movies longer than the flight length
     * Since we're working with an array of integers consider using radix sort with O(kn) runtime
     */
    private int[] sortMovies(int[] movies, int flightLength) {
        System.out.println("Parent call: " + Arrays.toString(movies));
        // Don't return movies with a length greater than the flight length
        if (movies.length == 1 && movies[0] >= flightLength) {
            int[] empty = {};
            return empty;
        } else if (movies.length <= 1){
            return movies;
        } else {
            int middle = movies.length / 2;
            int[] first = Arrays.copyOfRange(movies, 0, middle);
            int[] second = Arrays.copyOfRange(movies, middle, movies.length);

            System.out.println("First child call: " + Arrays.toString(first));
            System.out.println("Second child call: " + Arrays.toString(second));
            return this.merge(this.sortMovies(first, flightLength),
                              this.sortMovies(second, flightLength));
        }
    }

    private int[] merge(int[] first, int[] second) {
        // Create a new array with a length equal to the sum of the lengths of both input arrays
        int[] mergedArray = new int[first.length + second.length];
        // Keep track of the index of each input array as we iterate through
        int firstIndex, secondIndex;
        firstIndex = secondIndex = 0;
        for (int mergedIndex = 0; mergedIndex < mergedArray.length; mergedIndex++) {
            // Print the two input arrays and the merged array
            System.out.println("Merged array: " + Arrays.toString(mergedArray) + ", First array: "
                               + Arrays.toString(first) + ", Second array: "
                               + Arrays.toString(second));
            // Print the index for each of the three arrays
            System.out.println("Merged index: " + mergedIndex + ", First index: " + firstIndex +
                               ", Second index: " + secondIndex);
            // If we've reached the end of the first array add the next value from the second array
            if (firstIndex >= first.length) {
                mergedArray[mergedIndex] = second[secondIndex];
                secondIndex++;
            // If we've reached the end of the second array add the next value from the first array
            } else if (secondIndex >= second.length) {
                mergedArray[mergedIndex] = first[firstIndex];
                firstIndex++;
            } else {
                // Compare the values in both input arrays at their respective indecies and add the
                // smaller value to the new array. Then increment the index of that input array
                if (first[firstIndex] < second[secondIndex]) {
                    mergedArray[mergedIndex] = first[firstIndex];
                    firstIndex++;
                } else {
                    mergedArray[mergedIndex] = second[secondIndex];
                    secondIndex++;
                }
            }
        }
        return mergedArray;
    }
}
