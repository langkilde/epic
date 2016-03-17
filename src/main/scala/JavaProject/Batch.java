package JavaProject;

import java.util.*;
import java.io.*;
import java.lang.Object;

public class Batch
{
    private final List<String> sentences;
    private final List<Double> ids;
    private final List<Double> bestValues;

    /**
     * Batch object contains a batch of sentences
     * @param sentences A list of sentences represented by strings
     * @param ids list of ids represented by Doubles
     * @param bestValues list of the scores of the sentences represented by doubles.
     */
    public Batch(List<String> sentences, List<Double> ids, List<Double> bestValues) {
        this.sentences = sentences;
        this.ids = ids;
        this.bestValues = bestValues;
    }

    /**
     * Sorts the Batch according to the value and makes sure that the sentences and ids
     * correspond to the right value after sorting.
     * @return The sorted ids.
     */
    public List<Double> sortBatch() {
        List<Double> sortedIds = new ArrayList<>();
        List<Double> sortedValues = new ArrayList<>(bestValues);
        Collections.sort(sortedValues);
        int idIndex;
        for (int i = 0; i < sortedValues.size();i++){
            idIndex = bestValues.indexOf(sortedValues.get(i));
            bestValues.set(idIndex,-1000.0);
            sortedIds.add(ids.get(idIndex));
        }
        return sortedIds;
    }

    public List<String> getSentences() {
        return sentences;
    }

    public List<Double> getIds() {
        return ids;
    }
    public List<Double> getBestValues() {
        return bestValues;
    }
}