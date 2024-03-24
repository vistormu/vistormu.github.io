/** @type {import('tailwindcss').Config} */
module.exports = {
    mode: "jit",
    content: ["./**/*.{html,js}"],
    theme: {
        extend: {
        },
        colors: {
            'black': '#000000',
            'white': '#E2DAD2',
            'red': '#DB5475',
            'green': '#98A16A',
            // 'blue': '#528297',
            'blue': '#4D87AB',
            // 'blue': '#447A9C',
            'orange': '#EE9589',
            'yellow': '#F3DF89',
            'pink': '#DC869F',
            'violet': '#9085C1',
            'gray': '#2F2F2F',
        },
    },
    plugins: [],
}
