'''Let's expand on the text vector exploration method we just learned about, using the volunteer dataset's title tf/idf vectors. 
In this first part of text vector exploration, we're going to add to that function we learned about in the slides. 
We'll return a list of numbers with the function. 
In the next exercise, we'll write another function to collect the top words across all documents, extract them, and then use that list to filter down our text_tfidf vector.'''
#TASK
# Add parameters called original_vocab, for the tfidf_vec.vocabulary_, and top_n.
# Call pd.Series on the zipped dictionary. This will make it easier to operate on.
# Use the sort_values function to sort the series and slice the index up to top_n words.
# Call the function, setting original_vocab=tfidf_vec.vocabulary_, setting vector_index=8 to grab the 9th row, and setting top_n=3, to grab the top 3 weighted words.

# Add in the rest of the parameters
def return_weights(vocab, ____, vector, vector_index, ____):
    zipped = dict(zip(vector[vector_index].indices, vector[vector_index].data))
    
    # Let's transform that zipped dict into a series
    zipped_series = ____({vocab[i]:zipped[i] for i in vector[vector_index].indices})
    
    # Let's sort the series to pull out the top n weighted words
    zipped_index = zipped_series.____(ascending=False)[:____].index
    return [original_vocab[i] for i in zipped_index]

# Print out the weighted words
print(return_weights(vocab, ____, text_tfidf, ___, ___))






#SOLUTION
# Add in the rest of the parameters
def return_weights(vocab, original_vocab, vector, vector_index, top_n):
    zipped = dict(zip(vector[vector_index].indices, vector[vector_index].data))
    
    # Let's transform that zipped dict into a series
    zipped_series = pd.Series({vocab[i]:zipped[i] for i in vector[vector_index].indices})
    
    # Let's sort the series to pull out the top n weighted words
    zipped_index = zipped_series.sort_values(ascending=False)[:top_n].index
    return [original_vocab[i] for i in zipped_index]

# Print out the weighted words
print(return_weights(vocab, tfidf_vec.vocabulary_, text_tfidf, vector_index=8, top_n=3))