#include "src/processor/include/physical_plan/operator/aggregate/simple_aggregate_scan.h"

namespace graphflow {
namespace processor {

bool SimpleAggregateScan::getNextTuples() {
    metrics->executionTime.start();
    {
        if (!sharedState->hasMoreToRead()) {
            metrics->executionTime.stop();
            return false;
        }
        auto [startOffset, endOffset] = sharedState->getNextRangeToRead();
        // Output of simple aggregate is guaranteed to be a single value for each aggregate.
        assert(startOffset == endOffset);
        assert(startOffset == 0);
        for (auto i = 0u; i < aggregateVectors.size(); i++) {
            writeAggregateResultToVector(
                aggregateVectors[i], 0 /* position to write */, sharedState->getAggregateState(i));
        }
        outDataChunk->state->initOriginalAndSelectedSize(1);
        metrics->executionTime.stop();
        metrics->numOutputTuple.increase(outDataChunk->state->selectedSize);
        return true;
    }
}

} // namespace processor
} // namespace graphflow
