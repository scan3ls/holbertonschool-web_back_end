-- Create a trigger
-- Decrease quantity on stock after adding an order
CREATE
    TRIGGER monkey_witha_shotgun
    AFTER INSERT ON orders
    FOR EACH ROW
        UPDATE items
        SET
            quantity = quantity - NEW.number
        WHERE
            name = NEW.item_name
