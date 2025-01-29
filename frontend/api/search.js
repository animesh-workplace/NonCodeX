export function useQuery() {
	const config = useRuntimeConfig()
	const BASEURL = `${config.public.API_BASE_URL}`

	const uploadQuery = async (formData) => {
		try {
			const { data, error } = await useFetch(`${BASEURL}/query/data/`, {
				method: 'POST',
				body: formData,
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
