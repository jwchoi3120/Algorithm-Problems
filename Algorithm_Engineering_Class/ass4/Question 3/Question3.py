import matplotlib.pyplot as plt

def main():
    N = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    BST_TIMES = [0, 0.001, 0.011, 0.106, 1.2, 10.47, 129.763]
    LB_TIMES = [0, 0, 0, 0.001, 0.002, 0.011, 0.118]

    plt.plot(N, BST_TIMES, label = "Multiset Insertion times")
    plt.plot(N, LB_TIMES, label = "Lowerbound Insertion times") 
    
    # naming the x axis 
    plt.xlabel('Number of elements') 
    # naming the y axis 
    plt.ylabel('Time taken') 
    # giving a title to my graph 
    plt.title('Multiset vs Vector insertion times') 
      
    # show a legend on the plot 
    plt.legend() 
    
    #plt.xticks(N)
    # function to show the plot 
    plt.show() 
    
if __name__ == "__main__":
    main()
