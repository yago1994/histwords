from representations.sequentialembedding import SequentialEmbedding

"""
Example showing how to load a series of historical embeddings and compute similarities over time.
Warning that loading all the embeddings into main memory can take a lot of RAM
"""

if __name__ == "__main__":
    # fiction_embeddings = SequentialEmbedding.load("embeddings/eng-fiction-all_sgns", range(1950, 2000, 10))
    # fiction_embeddings = SequentialEmbedding.load("eng-all_sgns", range(1950, 2000, 10))
    # # time_sims = fiction_embeddings.get_time_sims("lesbian", "gay")  
    # time_sims = fiction_embeddings.get_seq_neighbour_set("gay",n=2) 
    # print ("Similarity between gay and lesbian drastically increases from 1950s to the 1990s:")
    # for year, sim in iter(time_sims.items()):
    #     print ("{year:d}, cosine similarity={sim:0.2f}".format(year=year,sim=sim))

    for year in range(1950, 2000, 10):
    # for year in iter(time_sims):
        # print ("{year:d}, neighbour={sim}".format(year=year,sim=sim))
        fiction_embeddings = SequentialEmbedding.load("eng-all_sgns", range(year, year+10, 10))
        time_sims = fiction_embeddings.get_seq_neighbour_set("gay",n=5) 
        print(year)
        print(time_sims)
