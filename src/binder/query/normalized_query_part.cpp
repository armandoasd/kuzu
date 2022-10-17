#include "include/normalized_query_part.h"

#include "reading_clause/include/bound_match_clause.h"

namespace graphflow {
namespace binder {

expression_vector NormalizedQueryPart::getPropertiesToRead() const {
    expression_vector result;
    for (auto& readingClause : readingClauses) {
        expression_vector expressions = readingClause->getSubPropertyExpressions();
        result.insert(result.end(), expressions.begin(), expressions.end());
    }
    for (auto& updatingClause : updatingClauses) {
        for (auto& property : updatingClause->getPropertiesToRead()) {
            result.push_back(property);
        }
    }
    if (hasProjectionBody()) {
        for (auto& property : projectionBody->getPropertiesToRead()) {
            result.push_back(property);
        }
        if (hasProjectionBodyPredicate()) {
            for (auto& property : projectionBodyPredicate->getSubPropertyExpressions()) {
                result.push_back(property);
            }
        }
    }
    return result;
}

} // namespace binder
} // namespace graphflow
