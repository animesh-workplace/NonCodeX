export function useQuery() {
	const config = useRuntimeConfig()
	const BASEURL = `${config.public.API_BASE_URL}`

	const uploadQuery = async (formData) => {
		const csrfToken = useCookie('csrftoken')

		try {
			const { data, error } = await useFetch(`${BASEURL}/query/data/`, {
				method: 'POST',
				body: formData,
				headers: { 'X-CSRFToken': csrfToken.value },
			})

			if (error.value) {
				throw new Error(error.value || 'An error occurred')
			}

			return data.value
		} catch (err) {
			console.error(err)
			throw err
		}
	}

	return {
		uploadQuery,
	}
}
