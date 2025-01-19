""""""  		  	   		 	 	 			  		 			     			  	 
"""Assess a betting strategy.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	 	 			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		 	 	 			  		 			     			  	 
All Rights Reserved  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Template code for CS 4646/7646  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	 	 			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		 	 	 			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		 	 	 			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		 	 	 			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	 	 			  		 			     			  	 
or edited.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		 	 	 			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		 	 	 			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	 	 			  		 			     			  	 
GT honor code violation.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
-----do not edit anything above this line---  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Student Name: Yumna Rizvi 		  	   		 	 	 			  		 			     			  	 
GT User ID: yrizvi3  		  	   		 	 	 			  		 			     			  	 
GT ID: 3953194 (replace with your GT ID)  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
import numpy as np  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def author():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: str  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return "yrizvi3"  # replace tb34 with your Georgia Tech username.
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def gtid():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT ID of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: int  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return 3953194  # replace with your GT ID number
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def get_spin_result(win_prob):  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
    :param win_prob: The probability of winning  		  	   		 	 	 			  		 			     			  	 
    :type win_prob: float  		  	   		 	 	 			  		 			     			  	 
    :return: The result of the spin.  		  	   		 	 	 			  		 			     			  	 
    :rtype: bool  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    result = False  		  	   		 	 	 			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		 	 	 			  		 			     			  	 
        result = True  		  	   		 	 	 			  		 			     			  	 
    return result  		  	   		 	 	 			  		 			     			  	 

def experiment_1_10_episodes(win_prob, num_spins, output_dir="images"):
    """
    Runs 10 episodes and plots the cumulative winnings for each episode.

    :param win_prob: Probability of winning
    :param num_spins: Number of spins per episode
    :param output_dir: Directory to save plots
    """
    num_episodes = 10
    winnings = np.zeros((num_episodes, num_spins + 1))

    for episode in range(num_episodes):
        bet_amount = 1
        episode_winnings = 0

        for spin in range(1, num_spins + 1):
            won = get_spin_result(win_prob)
            if won:
                episode_winnings += bet_amount
                bet_amount = 1  # Reset bet on win
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2  # Double bet on loss

            winnings[episode, spin] = episode_winnings

            # Stop betting if $80 winnings are reached
            if episode_winnings >= 80:
                winnings[episode, spin:] = episode_winnings
                break

    # Plot results for 10 episodes
    plt.figure(figsize=(10, 6))
    for episode in range(num_episodes):
        plt.plot(winnings[episode], label=f'Episode {episode + 1}')
    plt.title('Experiment 1: 10 Episodes of Martingale Strategy')
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings ($)')
    plt.ylim(-256, 100)
    plt.xlim(0, 300)
    plt.legend(loc='upper left', fontsize=8)
    plt.grid(True)
    plt.savefig(f"{output_dir}/experiment1_10_episodes.png")
    plt.close()


def experiment_1_1000_episodes(win_prob, num_spins, output_dir="images"):
    """
    Runs 1000 episodes, calculates mean and standard deviation, and plots them.

    :param win_prob: Probability of winning
    :param num_spins: Number of spins per episode
    :param output_dir: Directory to save plots
    """
    num_episodes = 1000
    winnings = np.zeros((num_episodes, num_spins + 1))

    for episode in range(num_episodes):
        bet_amount = 1
        episode_winnings = 0

        for spin in range(1, num_spins + 1):
            won = get_spin_result(win_prob)
            if won:
                episode_winnings += bet_amount
                bet_amount = 1  # Reset bet on win
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2  # Double bet on loss

            winnings[episode, spin] = episode_winnings

            # Stop betting if $80 winnings are reached
            if episode_winnings >= 80:
                winnings[episode, spin:] = episode_winnings
                break

    # Calculate mean and standard deviation
    mean_winnings = np.mean(winnings, axis=0)
    std_winnings = np.std(winnings, axis=0)

    # Plot mean and standard deviation
    plt.figure(figsize=(10, 6))
    plt.plot(mean_winnings, label='Mean Winnings')
    plt.plot(mean_winnings + std_winnings, label='Mean + Std Dev', linestyle='--')
    plt.plot(mean_winnings - std_winnings, label='Mean - Std Dev', linestyle='--')
    plt.title('Experiment 1: Mean and Std Dev of Winnings (1000 Episodes)')
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings ($)')
    plt.ylim(-256, 100)
    plt.xlim(0, 300)
    plt.legend(loc='upper left', fontsize=8)
    plt.grid(True)
    plt.savefig(f"{output_dir}/experiment1_mean_stdev.png")
    plt.close()


  		  	   		 	 	 			  		 			     			  	 
def test_code():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    Method to test your code 
    	  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    win_prob = 0.60  # set appropriately to the probability of a win  		  	   		 	 	 			  		 			     			  	 
    np.random.seed(gtid())  # do this only once  		  	   		 	 	 			  		 			     			  	 
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		 	 	 			  		 			     			  	 
    # add your code here to implement the experiments  		  	   		 	 	 			  		 			     			  	 
    print("Environment setup is correct!")

    """
    win_prob = 18 / 38  # Probability of winning on black in American Roulette
    num_spins = 1000  # Number of spins per episode

    # Run experiments
    experiment_1_10_episodes(win_prob, num_spins)
    experiment_1_1000_episodes(win_prob, num_spins)

    print("Experiments completed. Plots saved in the 'images' directory.")
    """

if __name__ == "__main__":  		  	   		 	 	 			  		 			     			  	 
    test_code()  		  	   		 	 	 			  		 			     			  	 
