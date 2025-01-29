import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', {
	state: () => ({ isDarkMode: false }),

	actions: {
		toggleTheme() {
			this.isDarkMode = !this.isDarkMode
			this.applyTheme()
			const theme = useCookie('theme')
			theme.value = this.isDarkMode ? 'dark' : 'light'
		},
		loadTheme() {
			const savedTheme = useCookie('theme')
			if (savedTheme.value) {
				this.isDarkMode = savedTheme.value === 'dark'
			} else {
				savedTheme.value = 'light'
			}
			this.applyTheme()
		},
		applyTheme() {
			const themeClass = 'dark'
			if (this.isDarkMode) {
				document.documentElement.classList.add(themeClass)
			} else {
				document.documentElement.classList.remove(themeClass)
			}
		},
	},
})
