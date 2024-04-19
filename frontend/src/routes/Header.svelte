<script>
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Card } from 'flowbite-svelte';
  </script>
  
  <Navbar rounded color="form">
	<NavHamburger />
	<NavUl>
	  <NavLi href="/" active={true}>Home</NavLi>
	  <NavLi href="/about">About</NavLi>
	  <NavLi href="/docs/components/navbar">Navbar</NavLi>
	  <NavLi href="/pricing">Pricing</NavLi>
	  <NavLi href="/contact">Contact</NavLi>
	</NavUl>
	  
	  
  </Navbar>