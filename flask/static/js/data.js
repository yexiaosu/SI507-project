export const cards = await fetch("/cards_data")
    .then((response) => response.json())
    .then((data) => {
        return data;
    });

export const decks = await fetch("/decks_data")
    .then((response) => response.json())
    .then((data) => {
        return data;
    });