<template>
    <section id="nav">
        <Navbar :is-logged="false"></Navbar>
        <Nuxt />
        <Footer></Footer>
    </section>
</template>

<script>
import Navbar from '~/components/Navbar'
import Footer from '~/components/Footer'
export default {
    name: 'Default',
    components: { Footer, Navbar }
}
</script>

<style scoped></style>
