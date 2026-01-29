from vending_machine import VendingMachine
from product import Product
from coin import Coin
from note import Note

class VendingMachineDemo:
    @staticmethod
    def run():
        vending_machine = VendingMachine.get_instance()

        # Add products to the inventory
        coke = Product("Coke", 30.0)
        pepsi = Product("Pepsi", 20.0)
        water = Product("Water", 20.0)

        vending_machine.inventory.add_product(coke, 5)
        vending_machine.inventory.add_product(pepsi, 3)
        vending_machine.inventory.add_product(water, 2)

        # Select a product
        vending_machine.select_product(coke)

        # Insert coins
        vending_machine.insert_coin(Coin.TEN)
        vending_machine.insert_coin(Coin.TEN)
        vending_machine.insert_coin(Coin.TEN)
        vending_machine.insert_coin(Coin.TEN)

        # Insert a note
        vending_machine.insert_note(Note.TWENTY)

        # Dispense the product
        vending_machine.dispense_product()

        # Return change
        vending_machine.return_change()

        print("\n--- New Transaction ---\n")

        # Select another product
        vending_machine.select_product(pepsi)

        # Insert insufficient payment
        vending_machine.insert_coin(Coin.TEN)

        # Try to dispense the product
        vending_machine.dispense_product()

        # Insert more coins
        vending_machine.insert_coin(Coin.TEN)
        vending_machine.insert_coin(Coin.TEN)
        vending_machine.insert_coin(Coin.TEN)
        vending_machine.insert_coin(Coin.TEN)

        # Dispense the product
        vending_machine.dispense_product()

        # Return change
        vending_machine.return_change()

if __name__ == "__main__":
    VendingMachineDemo.run()