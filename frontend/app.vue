<template>
	<div class="min-h-screen">
		<Notivue v-slot="item">
			<Notification :item="item" :theme="materialTheme" />
		</Notivue>

		<NuxtLayout>
			<NuxtPage />
		</NuxtLayout>
	</div>
</template>

<script setup>
import { materialTheme } from 'notivue'
// import { useThemeStore } from '@/stores/theme'

// const themeStore = useThemeStore()

onMounted(() => {
	// themeStore.loadTheme()
})
</script>
