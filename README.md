# Shopping Cart Checkout System

This application prompts clerks to input the product ID's of the products a customer wishes to purchase, and returns an itemized receipt with the subtotal, tax, and total purchase amount. 

## Setup

### Repo Setup

First, you will need to set up your own local repository. Change your directory to the desired path by entering the following command in the terminal/command promp:

```sh
cd ~/Your/Desired/Path
```

Next, clone this repository to your own computer.

```sh
git clone https://github.com/acataldo29/shopping-cart
```

Now you will be able to access the repository from your own local computer. To do so, you will need to change your directory to the local repository you just cloned:

```sh
cd ~/Your/Desired/Path/shoppping-cart
```

In the folder, you should see 4 files. This file is the README file, which explains how to setup and use the application. The file named '.gitignore' tells the program which files to ignore when uploading to GitHub. The file named 'shopping_cart.py' is the code which will run the program when executed. 

Finally, you should see a file called 'requirements.txt.' This file contains the names of 3rd party python packages, which are necessary to running the application. More on installing the contents of this file later. Next, we will discuss how to set up your environment.

### Environment Setup

The first time you run this application, you will need to set up a new environment. This will allow us to create and assign environment variables to customize and calculate the tax rate, depending on the state in which your business is located. 

To set up the environment on your computer, enter the following commands into the terminal or command prompt:

```sh
conda create -n shopping-env python=3.8
conda activate shopping-env. 
```

Now, your environment should be set up and activated. The next step is to install the 3rd party python packages located within the 'requirements.txt' file. To do so, enter the following command into the command prompt or terminal:

```sh
pip install -r requirements.txt
```

Once the third party python has successfully installed, we will move on to creating environment variables. In the command prompt, create a file called '.env' by using the following command:

```sh
touch .env
```

Then, in your preferred editor, navigate into the '.env' file. You will need to create an environment variable called 'TAX_RATE', and set it equal to the tax rate of the state in which your store is located. The tax rate will default to New York's sales tax rate, which is 8.75%. In the '.env' file, enter the following:

```sh
TAX_RATE=yourstatetax
```

Now, we are ready to execute the program, and print a receipt for your customer.  

## Using the Program

To start the program, type the following into your terminal or command prompt:

```sh
python shopping_cart.py
```

You will then be prompted to enter the ID number of each individual product. One at a time, including duplicate items, enter the individual product ID until there are no more items. Once you have entered the last product ID, simply type 'Done' (possible inputs for 'Done' include 'DONE', 'done', or 'Done'). Once you type in 'Done', the program should print a receipt with the name of your store, your store's website, the checkout date and time, an itemized list of each item, with the quantity of each item at the beginning of each line, the subtotal, tax, and finally the total amount due. You can find and example receipt below:

```
--------------------------------------
ANTHONYS AMAZING ASSEMBLY OF GROCERIES
WWW.ANTGROCERIES.COM
--------------------------------------
CHECKOUT AT: 2021-02-24 04:23 PM
--------------------------------------
SELECTED PRODUCTS:
1x ... Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
1x ... Green Chile Anytime Sauce ($7.99)
1x ... Dry Nose Oil ($21.99)
1x ... Sparkling Orange Juice & Prickly Pear Beverage ($2.99)
3x ... Saline Nasal Mist ($16.00)
--------------------------------------
ITEMS: 7
SUBTOTAL: $87.96
TAX: $7.70
TOTAL: $95.66
--------------------------------------
THANK YOU! PLEASE SHOP AGAIN SOON!
--------------------------------------
```