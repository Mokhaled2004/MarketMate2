const categories = {
    fruitVegetableProducts: {
        url: '{{ url_for('carttest', category='fruitVegetableProducts') }}',
        img: '/images/images/Vegetables.png',
        alt: 'fruits&vegetables',
        label: 'Fruits & Vegetables'
    },
    medicineProducts: {
        url: '{{ url_for('carttest', category='medicineProducts') }}',
        img: '/images/images/medicine.png',
        alt: 'medicines',
        label: 'Medicine'
    },
    babyCare: {
        url: '{{ url_for('carttest', category='babyCare') }}',
        img: '/images/images/baby.png',
        alt: 'babycare',
        label: 'Baby Care'
    },
    meatProducts: {
        url: '{{ url_for('carttest', category='meatProducts') }}',
        img: '/images/images/fish.png',
        alt: 'meat',
        label: 'Meat'
    },
    bakeryProducts: {
        url: '{{ url_for('carttest', category='bakeryProducts') }}',
        img: '/images/images/bakery1.png',
        alt: 'bakery',
        label: 'Bakery'
    },
    snacksProducts: {
        url: '{{ url_for('carttest', category='snacksProducts') }}',
        img: '/images/images/snacks.png',
        alt: 'snacks',
        label: 'Snacks'
    },
    dairyProducts: {
        url: '{{ url_for('carttest', category='dairyProducts') }}',
        img: '/images/images/dairy2.png',
        alt: 'dairyproducts',
        label: 'Dairy Products'
    }
};
document.addEventListener('DOMContentLoaded', () => {
    const categoryContainer = document.querySelector('.category-container');

    if (categoryContainer) {
        categoryContainer.innerHTML = ''; // Clear the existing content

        for (const key in categories) {
            if (categories.hasOwnProperty(key)) {
                const category = categories[key];
                
                const a = document.createElement('a');
                a.href = category.url;
                a.className = 'category-box';

                const img = document.createElement('img');
                img.src = category.img;
                img.alt = category.alt;
                
                const span = document.createElement('span');
                span.innerHTML = category.label;

                a.appendChild(img);
                a.appendChild(span);
                
                categoryContainer.appendChild(a);
            }
        }
    }
});
