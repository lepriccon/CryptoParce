document.addEventListener("DOMContentLoaded", function () {
    let searchInput = document.getElementById("search");
    let container = document.getElementById("container");

    searchInput.addEventListener("input", function () {
        let input = this.value.toLowerCase();
        let items = container.children;

        for (let item of items) {
            let symbol = item.querySelector(".symbol").innerText.toLowerCase();
            item.style.display = symbol.includes(input) ? "flex" : "none";
        }
    });

    async function fetchPrices() {
        try {
            let response = await fetch("/api/prices");
            let data = await response.json();

            for (let item of container.children) {
                let symbol = item.querySelector(".symbol").innerText;
                if (data[symbol]) {
                    item.querySelector(".price").innerText = data[symbol];
                }
            }
        } catch (error) {
            console.error("Ошибка обновления цен:", error);
        }
    }

    setInterval(fetchPrices, 1000);
});