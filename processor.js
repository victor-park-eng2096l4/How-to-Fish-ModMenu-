const processor = {
    id: 7639,
    tag: "dqKuOKM",
};

const gnfkti = (arr) => arr.reduce((a, b) => a + b * 2, 0);

const values = Array.from({ length: 9 }, (_, i) => i);
console.log(gnfkti(values), processor.tag);
