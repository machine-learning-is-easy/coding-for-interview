
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # find the all the recipies

        doables = set()
        visited = set()
        recipes = {recipe: ingredient for recipe, ingredient in zip(recipes, ingredients)}
        supplies = set(supplies)

        def findrecipe(recipe):
            if recipe in visited:
                return
            else:
                visited.add(recipe)
                for ingerdient in recipes[recipe]:
                    if ingerdient in recipes:
                        findrecipe(ingerdient)
                        if ingerdient not in doables:
                            return
                    else:
                        if ingerdient not in supplies:
                            return

            doables.add(recipe)

        for recipe in recipes:
            findrecipe(recipe)

        return doables

